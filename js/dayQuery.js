import postgres from 'postgres'


let sql;
export default class DayQuery {

  constructor() {
    sql = postgres('postgres://pguser:DTgXLPi1Urz7x6W4p3HCnd@127.0.0.1/pguser')

  }

  async singleDayTopSales(day) {
    if (!day.match(/^\d{4}-\d{2}-\d{2}$/)) {
      throw RangeError('Day expected in the format YYYY-MM-DD but got %s', day)
    }
    const result = await sql`SELECT theater, sum(amount) total
              FROM sale
              WHERE day = ${day}
              GROUP BY theater
              ORDER BY total DESC
              LIMIT 1;`

    return (result && result.length > 0) ? result[0] : null;
  }
}
