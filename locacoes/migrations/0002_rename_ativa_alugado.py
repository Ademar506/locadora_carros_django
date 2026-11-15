from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("locacoes", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="locacao",
            old_name="ativa",
            new_name="alugado",
        ),
    ]
