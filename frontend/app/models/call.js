import Model, { attr } from '@ember-data/model';

export default class CallModel extends Model {
  @attr username;
  @attr deceasedName;
  @attr dateOfDeath;
  @attr source;
  @attr callRating;
  @attr comment;
}
