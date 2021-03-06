import EmberRouter from '@ember/routing/router';
import config from 'frontend/config/environment';

export default class Router extends EmberRouter {
  location = config.locationType;
  rootURL = config.rootURL;
}

Router.map(function () {
  this.route('index');
  this.route('all-calls');
  this.route('calls');
  this.route('my-calls');
  this.route('call-detail');
  this.route('make-call');
  this.route('log-in');
  this.route('register');

});
