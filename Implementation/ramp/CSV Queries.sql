SELECT DISTINCT ON (finicity_institution_id)
	finicity_institution_id as f_id,
	tag,
	created_at
FROM TABLE t
WHERE t.is_deleted = False 
ORDER BY t.f_id, t.created_at ASC;
