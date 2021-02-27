import Model, { attr } from '@ember-data/model';

export default class CallModel extends Model {
  @attr username;
  @attr deceased;
  @attr dateOfDeath;
  @attr source;
  @attr image;
  @attr rating;
}
