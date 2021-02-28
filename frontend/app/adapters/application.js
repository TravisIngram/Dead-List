import JSONAPIAdapter from '@ember-data/adapter/json-api';

// import DS from 'ember-data';
// import { computed } from '@ember/object';

export default class ApplicationAdapter extends JSONAPIAdapter {
  host = 'http://localhost:8000';
  namespace = 'api';

}

// export default DS.RESTAdapter.extend({
//   host: computed(function(){
//     return 'http://localhost:8000';
//   }),
//   namespace: 'api'
// });