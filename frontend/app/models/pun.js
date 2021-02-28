import Model, { attr } from '@ember-data/model';

export default class PunModel extends Model {
  @attr username;
  @attr punContent;
  @attr punRating;
  @attr call;
}
