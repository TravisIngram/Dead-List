import Route from '@ember/routing/route';
import { inject as service } from '@ember/service';

export default class AllCallsRoute extends Route {
  @service store;

  async model() {
    return this.store.findAll('call');
  }
  // model() {
  //   return [
  //     {
  //       user: 'User #3',
  //       deceased: 'Hank Aaron',
	//       dateOfDeath: 'Jan 22, 2021',
	//       source: 'https://en.wikipedia.org/wiki/Hank_Aaron',
	//       image: 'https://en.wikipedia.org/wiki/Hank_Aaron#/media/File:Hank_Aaron_1974.jpg',
	//       rating: '2'
  //     },
  //     {
  //       user: 'User #3',
  //       deceased: 'Hank Aaron',
  //       dateOfDeath: 'Jan 22, 2021',
	//       source: 'https://en.wikipedia.org/wiki/Hank_Aaron',
	//       image: 'https://en.wikipedia.org/wiki/Hank_Aaron#/media/File:Hank_Aaron_1974.jpg',
	//       rating: '2'
  //     },
  //     {
  //       user: 'User #3',
  //       deceased: 'Hank Aaron',
  //       dateOfDeath: 'Jan 22, 2021',
	//       source: 'https://en.wikipedia.org/wiki/Hank_Aaron',
	//       image: 'https://en.wikipedia.org/wiki/Hank_Aaron#/media/File:Hank_Aaron_1974.jpg',
	//       rating: '2'
  //     },
  //     {
  //       user: 'User #3',
  //       deceased: 'Hank Aaron',
  //       dateOfDeath: 'Jan 22, 2021',
	//       source: 'https://en.wikipedia.org/wiki/Hank_Aaron',
	//       image: 'https://en.wikipedia.org/wiki/Hank_Aaron#/media/File:Hank_Aaron_1974.jpg',
	//       rating: '2'
  //     },
  //     {
  //       user: 'User #3',
  //       deceased: 'Hank Aaron',
  //       dateOfDeath: 'Jan 22, 2021',
	//       source: 'https://en.wikipedia.org/wiki/Hank_Aaron',
	//       image: 'https://en.wikipedia.org/wiki/Hank_Aaron#/media/File:Hank_Aaron_1974.jpg',
	//       rating: '2'
  //     }
  //   ]
  // }

}
