## Unique True vs. unique False

When creating a `ForeignKey` the only case where we would use a `unique=True` parameter is the case where they key passed to the row of the table must be unique in the whole table, i.e. there can not be two rows with the same value for the `ForeignKey`.

In our Application for the tables created so far no table should have such a `ForeignKey` as each `ForeignKey` can be used for different rows as multiple entries get created. If we would decide that a Farm can only be supplied by a single Storage and each Storage can only supply a single Farm we would change the `ForeignKey` to have a `unique=True` parameter.

## Example where `unique=True`

We have one Table (`Model`) containing basics information about the users such has username and password. We then have another Table containing information about the Main Address of each User. Each row in the table contains the address information (ZIP CODE, city, etc.) and the `UserID` indicating to which user the address belongs to. Each user can only have a single main address hence the `UerID` contained in each row must also be _unique_ for the whole Table: no two row can contain the same `UserId`. This type of relationship is called OneToOne relationship.
