automacro	waitforchat {
	party ""
	timeout 1
	priority 1
	call jumpto
}
macro jumpto {
	do c "@jumpto $.lastparty"
	stop
}