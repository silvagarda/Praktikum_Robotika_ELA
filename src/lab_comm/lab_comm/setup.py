entry_points={
        'console_scripts': [
            'sensor_publisher = lab_comm.sensor_publisher:main',
            'processing_node = lab_comm.processing_node:main',
            'reset_service = lab_comm.reset_service:main',
            'motion_action_server = lab_comm.motion_action_server:main',
        ],
    },
