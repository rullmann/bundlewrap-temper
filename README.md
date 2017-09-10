# temper

[TEMPer USB thermometers](http://pcsensor.com/usb-thermometers.html) are cheap and easy to use under Linux. This bundle receives [one of the many usb-thermometer](https://github.com/petervojtek/usb-thermometer) repositiries at GitHub, builds it and integrated with collectd if present.

## Requirements

* `libusb-devel`
  * Automatically installed if [dnf](https://github.com/rullmann/bundlewrap-dnf) is assigned to the node as well
* [item_git_deploy](https://github.com/bundlewrap/plugins/tree/master/item_git_deploy)

## Integrations

* Bundles:
  * [collectd](https://github.com/rullmann/bundlewrap-collectd)
    * Collect temperature regularly

## Metadata

* none
