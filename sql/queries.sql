-- ============================================
-- queries.sql
-- Requêtes d'analyse pour Looker Studio
-- ============================================

-- 1. KPIs globaux
SELECT
    COUNT(*) AS total_respondents,
    ROUND(AVG(stress_level), 2)      AS avg_stress,
    ROUND(AVG(anxiety_level), 2)     AS avg_anxiety,
    ROUND(AVG(addiction_level), 2)   AS avg_addiction,
    ROUND(AVG(sleep_hours), 2)       AS avg_sleep,
    ROUND(AVG(daily_social_media_hours), 2) AS avg_social_media,
    ROUND(100 * AVG(depression_label), 2) AS pct_depression
FROM `teen_mental_health.survey_responses`;


-- 2. Comparaison par plateforme
SELECT
    platform_usage,
    COUNT(*) AS respondents,
    ROUND(AVG(stress_level), 2)    AS avg_stress,
    ROUND(AVG(anxiety_level), 2)   AS avg_anxiety,
    ROUND(AVG(addiction_level), 2) AS avg_addiction,
    ROUND(AVG(sleep_hours), 2)     AS avg_sleep,
    ROUND(100 * AVG(depression_label), 2) AS pct_depression
FROM `teen_mental_health.survey_responses`
GROUP BY platform_usage
ORDER BY avg_stress DESC;


-- 3. Comparaison par tranche d'âge
SELECT
    age_group,
    COUNT(*) AS respondents,
    ROUND(AVG(daily_social_media_hours), 2) AS avg_social_media,
    ROUND(AVG(stress_level), 2)   AS avg_stress,
    ROUND(AVG(sleep_hours), 2)    AS avg_sleep,
    ROUND(AVG(academic_performance), 2) AS avg_gpa
FROM `teen_mental_health.survey_responses`
GROUP BY age_group
ORDER BY age_group;


-- 4. Comparaison par genre
SELECT
    gender,
    COUNT(*) AS respondents,
    ROUND(AVG(stress_level), 2)    AS avg_stress,
    ROUND(AVG(anxiety_level), 2)   AS avg_anxiety,
    ROUND(AVG(addiction_level), 2) AS avg_addiction,
    ROUND(100 * AVG(depression_label), 2) AS pct_depression
FROM `teen_mental_health.survey_responses`
GROUP BY gender;


-- 5. Relation temps d'écran / qualité du sommeil
SELECT
    screen_time_category,
    sleep_quality,
    COUNT(*) AS respondents,
    ROUND(AVG(stress_level), 2) AS avg_stress
FROM `teen_mental_health.survey_responses`
GROUP BY screen_time_category, sleep_quality
ORDER BY screen_time_category, sleep_quality;


-- 6. Top 10 des profils les plus à risque
SELECT
    respondent_id,
    age,
    gender,
    platform_usage,
    daily_social_media_hours,
    sleep_hours,
    mental_health_score,
    depression_label
FROM `teen_mental_health.survey_responses`
ORDER BY mental_health_score DESC
LIMIT 10;