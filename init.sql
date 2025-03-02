CREATE TABLE users (
  id char(36) NOT NULL,
  identifier varchar(255) NOT NULL,
  metadata json NOT NULL,
  createdAt varchar(255) DEFAULT NULL,
  PRIMARY KEY (id),
  UNIQUE KEY identifier (identifier)
);


CREATE TABLE threads (
  id char(36) NOT NULL,
  createdAt varchar(255) DEFAULT NULL,
  name varchar(255) DEFAULT NULL,
  userId char(36) DEFAULT NULL,
  userIdentifier varchar(255) DEFAULT NULL,
  tags json DEFAULT NULL,
  metadata json DEFAULT NULL,
  PRIMARY KEY (id),
  KEY userId (userId),
  CONSTRAINT threads_ibfk_1 FOREIGN KEY (userId) REFERENCES users (id) ON DELETE CASCADE
);


CREATE TABLE steps (
  id char(36) NOT NULL,
  name varchar(255) NOT NULL,
  type varchar(255) NOT NULL,
  threadId char(36) NOT NULL,
  parentId char(36) DEFAULT NULL,
  streaming tinyint(1) NOT NULL,
  waitForAnswer tinyint(1) DEFAULT NULL,
  isError tinyint(1) DEFAULT NULL,
  metadata json DEFAULT NULL,
  tags json DEFAULT NULL,
  input text,
  output text,
  createdAt varchar(255) DEFAULT NULL,
  start varchar(255) DEFAULT NULL,
  end varchar(255) DEFAULT NULL,
  generation json DEFAULT NULL,
  showInput text,
  language varchar(50) DEFAULT NULL,
  indent int DEFAULT NULL,
  PRIMARY KEY (id),
  KEY threadId (threadId)
);


CREATE TABLE elements (
  id char(36) NOT NULL,
  threadId char(36) DEFAULT NULL,
  type varchar(255) DEFAULT NULL,
  url text,
  chainlitKey varchar(255) DEFAULT NULL,
  name varchar(255) NOT NULL,
  display varchar(255) DEFAULT NULL,
  objectKey varchar(255) DEFAULT NULL,
  size varchar(50) DEFAULT NULL,
  page int DEFAULT NULL,
  language varchar(50) DEFAULT NULL,
  forId char(36) DEFAULT NULL,
  mime varchar(255) DEFAULT NULL,
  props json DEFAULT NULL,
  PRIMARY KEY (id),
  KEY threadId (threadId),
  CONSTRAINT elements_ibfk_1 FOREIGN KEY (threadId) REFERENCES threads (id) ON DELETE CASCADE
);


CREATE TABLE feedbacks (
  id char(36) NOT NULL,
  forId char(36) NOT NULL,
  threadId char(36) NOT NULL,
  value int NOT NULL,
  comment text,
  PRIMARY KEY (id),
  KEY threadId (threadId),
  CONSTRAINT feedbacks_ibfk_1 FOREIGN KEY (threadId) REFERENCES threads (id) ON DELETE CASCADE
);


CREATE TABLE themes (
  id int NOT NULL AUTO_INCREMENT,
  title varchar(255) NOT NULL,
  PRIMARY KEY (id),
  UNIQUE KEY themes_unique (title)
);


CREATE TABLE rounds (
  id int NOT NULL AUTO_INCREMENT,
  theme varchar(255) NOT NULL,
  start_timestamp timestamp NOT NULL,
  end_timestamp timestamp NOT NULL,
  time_duration int NOT NULL,
  PRIMARY KEY (id),
  KEY rounds_themes_FK (theme),
  CONSTRAINT rounds_themes_FK FOREIGN KEY (theme) REFERENCES themes (title) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO themes (title) VALUES
  ('Artificial Intelligence and Machine Learning'),
  ('Blockchain and Cryptocurrency'),
  ('Cloud Computing and DevOps'),
  ('Cybersecurity and Privacy'),
  ('Internet of Things (IoT)'),
  ('Mobile App Development'),
  ('Web Development'),
  ('Data Science and Analytics'),
  ('Software Architecture'),
  ('User Experience (UX) Design');
