# Generated by Django 3.1.4 on 2021-02-19 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rthl_site', '0042_actionpenalty_removal_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actiongoal',
            name='players',
        ),
        migrations.AddField(
            model_name='actiongoal',
            name='player_score',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='goal_main_player', to='rthl_site.player', verbose_name='Игрок, забивший гол'),
        ),
        migrations.AddField(
            model_name='actiongoal',
            name='players_passes',
            field=models.ManyToManyField(related_name='goal_notmain_players', to='rthl_site.Player', verbose_name='Игроки, сделавшие пас'),
        ),
    ]
