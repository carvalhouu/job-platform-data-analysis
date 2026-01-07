CREATE TABLE users (
  user_id INTEGER PRIMARY KEY,
  age INTEGER,
  country TEXT,
  education_level TEXT,
  signup_date DATE
);

CREATE TABLE companies (
  company_id INTEGER PRIMARY KEY,
  industry TEXT,
  country TEXT
);

CREATE TABLE jobs (
  job_id INTEGER PRIMARY KEY,
  company_id INTEGER,
  job_type TEXT,
  location TEXT,
  salary_range TEXT,
  FOREIGN KEY (company_id) REFERENCES companies(company_id)
);

CREATE TABLE applications (
  application_id INTEGER PRIMARY KEY,
  user_id INTEGER,
  job_id INTEGER,
  application_date DATE,
  status TEXT,
  FOREIGN KEY (user_id) REFERENCES users(user_id),
  FOREIGN KEY (job_id) REFERENCES jobs(job_id)
);

