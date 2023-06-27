UPDATE salary
SET sex = 
	CASE sex 
        when 'f' then 'm' 
        when 'm' then 'f' 
    END;