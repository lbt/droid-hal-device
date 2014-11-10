# device is the codename for the device
# eg mako = Nexus 4
%define device baytrail_generic
# vendor is used in device/%vendor/%device/
%define vendor intel

# Manufacturer and device name to be shown in UI
%define vendor_pretty Intel
%define device_pretty NUC

# This not an armv7hl so be explicit
%define device_target_cpu i586

%define device_variant -eng

%include rpm/droid-hal-device.inc

