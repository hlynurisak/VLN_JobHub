-- Creating the Company table
CREATE TABLE company_company (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    advertisement_created TIMESTAMP NOT NULL,
    logo VARCHAR(9999)
);

-- Creating the JobCategory table
CREATE TABLE JobHub_jobcategory (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Creating the Job table
CREATE TABLE JobHub_job (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description VARCHAR(255),
    company_id INT NOT NULL,
    category_id INT NOT NULL,
    FOREIGN KEY (company_id) REFERENCES company_company(id),
    FOREIGN KEY (category_id) REFERENCES JobHub_jobcategory(id)
);

-- Creating the CompanyImage table
CREATE TABLE JobHub_companyimage (
    id SERIAL PRIMARY KEY,
    name VARCHAR(9999) NOT NULL,
    job_id INT NOT NULL,
    FOREIGN KEY (job_id) REFERENCES JobHub_job(id)
);

-- Insert data into Company
INSERT INTO company_company (name, advertisement_created, logo) VALUES
('Tech Innovations', '2024-05-13 09:00:00', 'tech_innovations_logo.png'),
('Green Energy Inc.', '2024-05-13 10:00:00', 'green_energy_logo.png'),
('MediCare Solutions', '2024-05-13 11:00:00', 'medicare_solutions_logo.png');

-- Insert data into JobCategory
INSERT INTO JobHub_jobcategory (name) VALUES
('Engineering'),
('Project Management'),
('Analytics'),
('Healthcare');

-- Assuming company IDs and category IDs as previously set up
-- Insert data into Job
INSERT INTO JobHub_job (name, description, company_id, category_id) VALUES
('Software Engineer', 'Develop innovative software solutions using AI.', 1, 1),
('Project Manager', 'Manage large scale renewable projects.', 2, 2),
('Data Analyst', 'Analyze healthcare data for insights.', 3, 3),
('Biomedical Engineer', 'Develop new medical devices.', 3, 4);

-- Insert data into CompanyImage
-- Assuming job IDs correctly correlate with previously inserted jobs
INSERT INTO JobHub_companyimage (name, job_id) VALUES
('office_view.png', 1),
('project_site_view.png', 2),
('lab_equipment.png', 4);
