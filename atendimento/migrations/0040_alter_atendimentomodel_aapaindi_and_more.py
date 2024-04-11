# Generated by Django 5.0.1 on 2024-03-17 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atendimento', '0039_audiometriamodel_aucoordenadas_planoii_linha1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aApaIndi',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Aparelho Indicado'),
        ),
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aCancerO',
            field=models.BooleanField(blank=True, default=False, verbose_name='(Doenças) Câncer'),
        ),
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aCardiop',
            field=models.BooleanField(blank=True, default=False, verbose_name='(Doenças) Cardiopatia (problema de coração)'),
        ),
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aCineTea',
            field=models.BooleanField(blank=True, default=False, verbose_name='(Dificuldades) Cinema / Teatro'),
        ),
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aCiruOuv',
            field=models.BooleanField(blank=True, default=False, verbose_name='(Percepções) Cirurgia nos ouvidos'),
        ),
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aClikOOD',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Click Ouvido Direito'),
        ),
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aClikOOE',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Click Ouvido Esquerdo'),
        ),
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aCoceira',
            field=models.BooleanField(blank=True, default=False, verbose_name='(Percepções) Coceira'),
        ),
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aColeAlt',
            field=models.BooleanField(blank=True, default=False, verbose_name='(Doenças) Colesterol Alto'),
        ),
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aComClik',
            field=models.CharField(blank=True, choices=[('sim', 'Sim'), ('não', 'Não')], max_length=5, null=True, verbose_name='c/ Click'),
        ),
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aConhece',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Onde conheceu a MARKI?'),
        ),
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aConvGru',
            field=models.BooleanField(blank=True, default=False, verbose_name='(Dificuldades) Conversa com grupo de pessoas'),
        ),
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aConvRui',
            field=models.BooleanField(blank=True, default=False, verbose_name='(Dificuldades) Conversa em ambiente ruidoso'),
        ),
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aDiabete',
            field=models.BooleanField(blank=True, default=False, verbose_name='(Doenças) Diabetes'),
        ),
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aDifiEsc',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Tem dificuldade para escutar?'),
        ),
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aDifiPio',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Sua dificuldade está piorando?'),
        ),
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aDorOOOO',
            field=models.BooleanField(blank=True, default=False, verbose_name='(Percepções) Dor'),
        ),
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aFalaBai',
            field=models.BooleanField(blank=True, default=False, verbose_name='(Dificuldades) Fala muito baixa'),
        ),
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aFaladis',
            field=models.BooleanField(blank=True, default=False, verbose_name='(Dificuldades) Fala à distância'),
        ),
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aFormPag',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Forma de Pagamento'),
        ),
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aJaTesAp',
            field=models.CharField(blank=True, choices=[('sim', 'Sim'), ('não', 'Não')], max_length=5, null=True, verbose_name='Já testou aparelho?'),
        ),
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aJaUsoAp',
            field=models.CharField(blank=True, choices=[('sim', 'Sim'), ('não', 'Não')], max_length=5, null=True, verbose_name='Já usou aparelho antes?'),
        ),
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aLabirin',
            field=models.BooleanField(blank=True, default=False, verbose_name='(Doenças) Labirintite'),
        ),
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aLadoInd',
            field=models.CharField(blank=True, choices=[('OE', 'Ouvido Esquerdo'), ('OD', 'Ouvido Direito'), ('Ambos', 'Ambos')], max_length=50, null=True, verbose_name='Lado Indicado'),
        ),
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aMarcaOO',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Marca / Modelo Aparelho'),
        ),
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aOtiteOO',
            field=models.BooleanField(blank=True, default=False, verbose_name='(Percepções) Otite'),
        ),
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aOutrDif',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='(Dificuldades) Outras'),
        ),
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aOutrDoe',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='(Doenças) Outras'),
        ),
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aOutrOuv',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='(Percepções) Outros'),
        ),
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aOuviMel',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Tem algum ouvido que escuta melhor?'),
        ),
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aPaleSal',
            field=models.BooleanField(blank=True, default=False, verbose_name='(Dificuldades) Palestra / Sala de aula'),
        ),
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aPessFam',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Há pessoas na sua família com perda de Audição?'),
        ),
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aPresAlt',
            field=models.BooleanField(blank=True, default=False, verbose_name='(Doenças) Pressão Alta'),
        ),
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aProbRin',
            field=models.BooleanField(blank=True, default=False, verbose_name='(Doenças) Problemas nos rins'),
        ),
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aProbTir',
            field=models.BooleanField(blank=True, default=False, verbose_name='(Doenças) Problema na Tireoide'),
        ),
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aQualApa',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Qual aparelho já testou?'),
        ),
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aReceOOD',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Receptor Ouvido Direito'),
        ),
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aReceOOE',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Receptor Ouvido Esquerdo'),
        ),
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aRetTest',
            field=models.DateField(blank=True, null=True, verbose_name='Data de Retorno de teste'),
        ),
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aSaiTest',
            field=models.DateField(blank=True, null=True, verbose_name='Data de Saída para teste'),
        ),
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aSemClik',
            field=models.CharField(blank=True, choices=[('sim', 'Sim'), ('não', 'Não')], max_length=5, null=True, verbose_name='s/ click'),
        ),
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aSensTam',
            field=models.BooleanField(blank=True, default=False, verbose_name='(Percepções) Sensação de ouvido tampado'),
        ),
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aTeleCel',
            field=models.BooleanField(blank=True, default=False, verbose_name='(Dificuldades) Celular'),
        ),
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aTeleFix',
            field=models.BooleanField(blank=True, default=False, verbose_name='(Dificuldades) Telefone Fixo'),
        ),
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aTelevis',
            field=models.BooleanField(blank=True, default=False, verbose_name='(Dificuldades) Televisão'),
        ),
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aTempoOO',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Tempo de uso aparelho'),
        ),
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aTimpPer',
            field=models.BooleanField(blank=True, default=False, verbose_name='(Percepções) Tímpano perfurado'),
        ),
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aTontura',
            field=models.BooleanField(blank=True, default=False, verbose_name='(Doenças) Tonturas'),
        ),
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aTrabRui',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Já trabalhou em Ambiente Ruidoso?'),
        ),
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aTuboOOD',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Tubo Ouvido Direito'),
        ),
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aTuboOOE',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Tubo Ouvido Esquerdo'),
        ),
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aUsoOtot',
            field=models.BooleanField(blank=True, default=False, verbose_name='(Doenças) Uso de ototóxico (antibiótico forte)'),
        ),
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aValApar',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Valor aparelho'),
        ),
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aZumbido',
            field=models.BooleanField(blank=True, default=False, verbose_name='(Percepções) Zumbido'),
        ),
    ]