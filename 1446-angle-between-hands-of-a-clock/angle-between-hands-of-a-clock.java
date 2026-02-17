class Solution {
    public double angleClock(int hour, int minutes) {
        double hr = ((360.0 / 12) * hour) + (((360.0/12)/60*minutes));
        double min = (360.0/60) * minutes;
        double abs = Math.abs(hr-min);
        return Math.min(360-abs, abs);
    }
}