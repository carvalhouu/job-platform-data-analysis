-- Query 1: Total de candidaturas por vaga
SELECT 
  job_id,
  COUNT(*) AS total_applications
FROM applications
GROUP BY job_id
ORDER BY total_applications DESC;

-- Query 2: Taxa de aprovação por vaga
SELECT
  job_id,
  COUNT(CASE WHEN status = 'approved' THEN 1 END) * 1.0 / COUNT(*) AS approval_rate
FROM applications
GROUP BY job_id;

-- Query 3: Usuários mais ativos
SELECT
  user_id,
  COUNT(*) AS total_applications
FROM applications
GROUP BY user_id
ORDER BY total_applications DESC
LIMIT 10;

-- Query 4: Candidaturas por país
SELECT
  u.country,
  COUNT(*) AS total_applications
FROM applications a
JOIN users u ON a.user_id = u.user_id
GROUP BY u.country
ORDER BY total_applications DESC;

-- Query 5: Vagas por setor
SELECT
  c.industry,
  COUNT(j.job_id) AS total_jobs
FROM jobs j
JOIN companies c ON j.company_id = c.company_id
GROUP BY c.industry
ORDER BY total_jobs DESC;

-- Query 6: Tempo médio até candidatura
SELECT
  AVG(JULIANDAY(application_date) - JULIANDAY(signup_date)) AS avg_days_to_apply
FROM applications a
JOIN users u ON a.user_id = u.user_id;

