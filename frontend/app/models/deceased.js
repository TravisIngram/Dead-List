import Model, { attr } from '@ember-data/model';

export default class DeceasedModel extends Model {
  @attr deceasedName;
  @attr biography;
  @attr source;
  @attr dateOfDeath;

}
