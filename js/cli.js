import DayQuery from './dayQuery.js'
import prompts from 'prompts';

const dayQuery = new DayQuery();

(async () => {

  while (true) {
    let day = (await prompts({
      type: 'text',
      name: 'day',
      message: 'What day?',
    })).day;
    console.log(typeof (day))
    let result = await dayQuery.singleDayTopSales(day);

    console.log({ day, ...result });

    if (
      !(await prompts({
        type: 'toggle', name: 'v', message: 'Again?', initial: true, active: 'yes', inactive: 'no'
      })).v) {
        console.info('K. bye!')
        process.exit(0);
    }
  }
})();
