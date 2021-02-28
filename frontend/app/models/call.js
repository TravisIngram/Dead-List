import Model, { attr } from '@ember-data/model';

export default class CallModel extends Model {
  @attr('number') username;
  @attr('string') deceasedName;
  @attr('string') dateOfDeath;
  @attr('string') source;
  @attr('number') callRating;
  @attr('string') comment;
}


// @attr username;
// @attr deceasedName;
// @attr dateOfDeath;
// @attr source;
// @attr callRating;
// @attr comment;