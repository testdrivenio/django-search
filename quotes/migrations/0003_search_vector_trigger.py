from django.contrib.postgres.search import SearchVector
from django.db import migrations


def compute_search_vector(apps, schema_editor):
    Quote = apps.get_model("quotes", "Quote")
    Quote.objects.update(search_vector=SearchVector("name", "quote"))


class Migration(migrations.Migration):

    dependencies = [
        ("quotes", "0002_quote_search_vector"),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
            CREATE TRIGGER search_vector_trigger
            BEFORE INSERT OR UPDATE OF name, quote, search_vector
            ON quotes_quote
            FOR EACH ROW EXECUTE PROCEDURE
            tsvector_update_trigger(
                search_vector, 'pg_catalog.english', name, quote
            );
            UPDATE quotes_quote SET search_vector = NULL;
            """,
            reverse_sql="""
            DROP TRIGGER IF EXISTS search_vector_trigger
            ON quotes_quote;
            """,
        ),
        migrations.RunPython(
            compute_search_vector, reverse_code=migrations.RunPython.noop
        ),
    ]
