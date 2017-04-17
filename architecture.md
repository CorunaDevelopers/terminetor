REST  ->   

	heater.schedule_week(from, to, temp) - inform job (actor)
	heater.on(timeout) - 
	heater.off()

	report service -- (heater control nodes, sensor nodes)
		getHeaterHistory
		getTempHistory
		getHumHistory
		setInterval(minutes)



	heater service --  (heater control node, sensor nodes, display nodes)
		add schedule
		get schedules
		get status
		set target temo
		on (time: Optional)
		off (num days: Optional)


		QUEUE

	heater control node - on, off, temp, status
	sensor node - read temp, read hum, read lum
    display node - show temp, show hum, show heater status, show target temp, 
