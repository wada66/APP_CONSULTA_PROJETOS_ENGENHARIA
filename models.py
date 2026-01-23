from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Tabelas principais
class Setor(db.Model):
    __tablename__ = 'setor'
    id_setor = db.Column(db.Integer, primary_key=True)
    nome_setor = db.Column(db.String(150))
    projens = db.relationship('Projen', backref='setor', lazy=True)

class Local(db.Model):
    __tablename__ = 'local'
    id_local = db.Column(db.Integer, primary_key=True)
    nome_local = db.Column(db.String(150))
    projens = db.relationship('Projen', backref='local', lazy=True)

class Projen(db.Model):
    __tablename__ = 'projen'
    id_projen = db.Column(db.Integer, primary_key=True)
    n_chamada_projen = db.Column(db.String(10))
    titulo_projen = db.Column(db.String(500))
    local_id = db.Column(db.Integer, db.ForeignKey('local.id_local'))
    data_projen = db.Column(db.Date)
    colacao_pag_projen = db.Column(db.String(20))
    colacao_volume_tomo_projen = db.Column(db.String(20))
    conteudo_projen = db.Column(db.String(1000))
    notas_gerais_projen = db.Column(db.String(500))
    setor_id = db.Column(db.Integer, db.ForeignKey('setor.id_setor'))
    fonte_projen = db.Column(db.String(200))
    
    # Relacionamentos muitos-para-muitos
    assuntos = db.relationship('Assunto', secondary='projen_assunto', backref='projens')
    executores = db.relationship('Executor', secondary='projen_executor', backref='projens')
    areas_geograficas = db.relationship('AreaGeografica', secondary='projen_area_geografica', backref='projens')
    autores = db.relationship('Autor', secondary='projen_autor', backref='projens')

# Tabelas auxiliares
class Assunto(db.Model):
    __tablename__ = 'assunto'
    id_assunto = db.Column(db.Integer, primary_key=True)
    nome_assunto = db.Column(db.String(300))

class Executor(db.Model):
    __tablename__ = 'executor'
    id_executor = db.Column(db.Integer, primary_key=True)
    nome_executor = db.Column(db.String(200))

class AreaGeografica(db.Model):
    __tablename__ = 'area_geografica'
    id_area_geografica = db.Column(db.Integer, primary_key=True)
    nome_area_geografica = db.Column(db.String(150))

class Autor(db.Model):
    __tablename__ = 'autor'
    id_autor = db.Column(db.Integer, primary_key=True)
    nome_autor = db.Column(db.String(200))
    tipo_autor = db.Column(db.String(12))

# Tabelas de junção
class ProjenAssunto(db.Model):
    __tablename__ = 'projen_assunto'
    id_projen_assunto = db.Column(db.Integer, primary_key=True)
    projen_id = db.Column(db.Integer, db.ForeignKey('projen.id_projen'))
    assunto_id = db.Column(db.Integer, db.ForeignKey('assunto.id_assunto'))

class ProjenExecutor(db.Model):
    __tablename__ = 'projen_executor'
    id_projen_executor = db.Column(db.Integer, primary_key=True)
    projen_id = db.Column(db.Integer, db.ForeignKey('projen.id_projen'))
    executor_id = db.Column(db.Integer, db.ForeignKey('executor.id_executor'))

class ProjenAreaGeografica(db.Model):
    __tablename__ = 'projen_area_geografica'
    id_projen_area_geografica = db.Column(db.Integer, primary_key=True)
    projen_id = db.Column(db.Integer, db.ForeignKey('projen.id_projen'))
    area_geografica_id = db.Column(db.Integer, db.ForeignKey('area_geografica.id_area_geografica'))

class ProjenAutor(db.Model):
    __tablename__ = 'projen_autor'
    id_projen_autor = db.Column(db.Integer, primary_key=True)
    projen_id = db.Column(db.Integer, db.ForeignKey('projen.id_projen'))
    autor_id = db.Column(db.Integer, db.ForeignKey('autor.id_autor'))