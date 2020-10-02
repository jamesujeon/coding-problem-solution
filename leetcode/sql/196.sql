-- 문제 링크: https://leetcode.com/problems/delete-duplicate-emails/

DELETE FROM Person
WHERE Id != (
    SELECT Id
    FROM (SELECT * FROM Person) P
    WHERE Email = Person.Email
    ORDER BY Id
    LIMIT 1
)
