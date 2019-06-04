const char * name = "trig_dist"
enum wrtd_status status;
struct wrtd_dev *wrtd; //WRTD device returned by the wrtd_init
struct wrtd_tstamp ts;
ts.seconds = 0;
ts.ns = 500;
ts.frac = 0;

status = wrtd_add_rule(wrtd, name);
WRTD_RETURN_IF_ERROR(status);

status = wrtd_set_attr_string(wrtd, name, WRTD_ATTR_RULE_SOURCE, LC-I0);
WRTD_RETURN_IF_ERROR(status);

status = wrtd_set_attr_string(wrtd, name, WRTD_ATTR_RULE_DESTINATION, LAN1);
WRTD_RETURN_IF_ERROR(status);

status = wrtd_set_attr_tstamp(wrtd, name, WRTD_ATTR_RULE_DELAY, &ts);
WRTD_RETURN_IF_ERROR(status);

status = wrtd_set_attr_bool(wrtd, name, WRTD_ATTR_RULE_ENABLED, 1);
WRTD_RETURN_IF_ERROR(status);

const char * name = "trig_rec"
enum wrtd_status status;
struct wrtd_dev *wrtd; //WRTD device returned by the wrtd_init
struct wrtd_tstamp ts;
ts.seconds = 0;
ts.ns = 0;
ts.frac = 0;

status = wrtd_add_rule(wrtd, name);
WRTD_RETURN_IF_ERROR(status);

status = wrtd_set_attr_string(wrtd, name, WRTD_ATTR_RULE_SOURCE, LAN1);
WRTD_RETURN_IF_ERROR(status);

status = wrtd_set_attr_string(wrtd, name, WRTD_ATTR_RULE_DESTINATION, LC-O0);
WRTD_RETURN_IF_ERROR(status);

status = wrtd_set_attr_tstamp(wrtd, name, WRTD_ATTR_RULE_DELAY, &ts);
WRTD_RETURN_IF_ERROR(status);

status = wrtd_set_attr_bool(wrtd, name, WRTD_ATTR_RULE_ENABLED, 1);
WRTD_RETURN_IF_ERROR(status);


