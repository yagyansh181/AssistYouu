import struct
from datetime import datetime
import time
from playsound import playsound
import pyaudio
import arduinointerference as ai
from binding.python.porcupine import Porcupine


porcupine_wakeword = None
pa = None
audio_stream = None
awake = False
start_time = None
wake_time = 6500  # ms

try:
    porcupine_wakeword = Porcupine(library_path='lib/windows/amd64/libpv_porcupine.dll',
                                   model_file_path='lib/common/porcupine_params.pv',
                                   keyword_file_paths=['resources/keyword_files/home-auto/hey christina_windows.ppn'],
                                   sensitivities=[0.9])

    porcupine_commands = Porcupine(library_path='lib/windows/amd64/libpv_porcupine.dll',
                                   model_file_path='lib/common/porcupine_params.pv',
                                   keyword_file_paths=[
                                       'resources/keyword_files/home-auto/room ac_windows.ppn',
                                       'resources/keyword_files/home-auto/room lights_windows.ppn',
                                       'resources/keyword_files/home-auto/hall lights_windows.ppn',
                                       'resources/keyword_files/home-auto/garden lights_windows.ppn',
                                       'resources/keyword_files/home-auto/porch lights_windows.ppn',
                                       'resources/keyword_files/home-auto/stairs lights_windows.ppn',
                                       'resources/keyword_files/home-auto/bathroom geyser_windows.ppn',
                                       'resources/keyword_files/home-auto/water pump_windows.ppn',
                                       'resources/keyword_files/home-auto/socket one_windows.ppn',
                                       'resources/keyword_files/home-auto/socket two_windows.ppn',
                                       'resources/keyword_files/home-auto/open the door_windows.ppn',
                                       'resources/keyword_files/home-auto/close the door_windows.ppn',
                                       'resources/keyword_files/home-auto/mains on_windows.ppn',
                                       'resources/keyword_files/home-auto/mains off_windows.ppn'
                                   ],
                                   sensitivities=[0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90,
                                                  0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90])

    pa = pyaudio.PyAudio()
    audio_stream = pa.open(
        rate=porcupine_wakeword.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine_wakeword.frame_length)
    print("Assistant is UP and running,ready to take wake commands")
    while True:
        pcm = audio_stream.read(porcupine_wakeword.frame_length)
        pcm = struct.unpack_from("h" * porcupine_wakeword.frame_length, pcm)

        if not awake:
            # print('...')

            result = porcupine_wakeword.process(pcm)
            if result:
                awake = True
                playsound("sounds/hey_how_can_i_help_you.mp3")
                start_time = time.time()
                print('Voice Assistant activated, give command...')
                playsound("sounds/assistant_wake.mp3")
                command_result = None;
        else:
            if (time.time() - start_time) * 1000 > wake_time:
                print('Voice assistant going back to sleep')
                playsound("sounds/assistant_sleep.mp3")
                awake = False
            command_result = porcupine_commands.process(pcm)
            if command_result >= 0:
                print('{} detected command: {}'.format(str(datetime.now()), command_result))

                # if command_result == 0:
                #
                #     print('Turning off AC Hall')
                #     playsound("sounds/turning_off_ac_hall.mp3")
                #     time.sleep(1)
                #     playsound("sounds/device_down.mp3")
                #
                # elif command_result == 1:
                #
                #     print('Turning ON AC Hall')
                #     playsound("sounds/turning_on_ac_hall.mp3")
                #     time.sleep(1)
                #     playsound("sounds/device_up.mp3")
                #     command_result = "";

                if command_result == 0:

                    u = 'u2'
                    d = 'd2'

                    if ai.state[2] == 1:
                        ai.command(d)
                        print('Turning off AC Room')
                        playsound("sounds/turning_off_ac_room.mp3")
                        time.sleep(1)
                        playsound("sounds/device_down.mp3")
                        command_result = ""

                    elif ai.state[2] == 0:
                        ai.command(u)
                        print('Turning on AC Room')
                        playsound("sounds/turning_on_ac_room.mp3")
                        time.sleep(1)
                        playsound("sounds/device_up.mp3")
                        command_result = ""

                elif command_result == 1:

                    u = 'u3'
                    d = 'd3'

                    if ai.state[3] == 1:
                        ai.command(d)
                        print('Turning off Room Lights')
                        playsound("sounds/turning_off_the_room_lights.mp3")
                        time.sleep(1)
                        playsound("sounds/device_down.mp3")
                        command_result = ""

                    elif ai.state[3] == 0:
                        ai.command(u)
                        print('Turning on Room Lights')
                        playsound("sounds/turning_on_the_room_lights.mp3")
                        time.sleep(1)
                        playsound("sounds/device_up.mp3")
                        command_result = ""

                elif command_result == 2:

                    u = 'u4'
                    d = 'd4'

                    if ai.state[4] == 1:
                        ai.command(d)
                        print('Turning off Hall Lights')
                        playsound("sounds/turning_off_the_hall_lights.mp3")
                        time.sleep(1)
                        playsound("sounds/device_down.mp3")
                        command_result = ""

                    elif ai.state[4] == 0:
                        ai.command(u)
                        print('Turning on Hall Lights')
                        playsound("sounds/turning_on_the_hall_lights.mp3")
                        time.sleep(1)
                        playsound("sounds/device_up.mp3")
                        command_result = ""

                elif command_result == 3:

                    u = 'u5'
                    d = 'd5'

                    if ai.state[5] == 1:
                        ai.command(d)
                        print('Turning off Garden Lights')
                        playsound("sounds/turning_off_garden_lights.mp3")
                        time.sleep(1)
                        playsound("sounds/device_down.mp3")
                        command_result = ""

                    elif ai.state[5] == 0:
                        ai.command(u)
                        print('Turning on Garden Lights')
                        playsound("sounds/lighting_up_the_garden.mp3")
                        time.sleep(1)
                        playsound("sounds/device_up.mp3")
                        command_result = ""

                elif command_result == 4:

                    u = 'u6'
                    d = 'd6'

                    if ai.state[6] == 1:
                        ai.command(d)
                        print('Turning off Porch Lights')
                        playsound("sounds/turning_off_the_porch_lights.mp3")
                        time.sleep(1)
                        playsound("sounds/device_down.mp3")
                        command_result = ""

                    elif ai.state[6] == 0:
                        ai.command(u)
                        print('Turning on Porch Lights')
                        playsound("sounds/turning_on_the_porch_lights.mp3")
                        time.sleep(1)
                        playsound("sounds/device_up.mp3")
                        command_result = ""

                elif command_result == 5:

                    u = 'u7'
                    d = 'd7'

                    if ai.state[7] == 1:
                        ai.command(d)
                        print('Turning off Stairs Lights')
                        playsound("sounds/turning_off_stairs_lights.mp3")
                        time.sleep(1)
                        playsound("sounds/device_down.mp3")
                        command_result = ""

                    elif ai.state[7] == 0:
                        ai.command(u)
                        print('Turning on Stairs Lights')
                        playsound("sounds/turning_on_stairs_lights.mp3")
                        time.sleep(1)
                        playsound("sounds/device_up.mp3")
                        command_result = ""

                elif command_result == 6:

                    u = 'u8'
                    d = 'd8'

                    if ai.state[7] == 1:
                        ai.command(d)
                        print('Turning off Bathroom Geyser')
                        playsound("sounds/turning_off_the_geyser.mp3")
                        time.sleep(1)
                        playsound("sounds/device_down.mp3")
                        command_result = ""

                    elif ai.state[7] == 0:
                        ai.command(u)
                        print('Turning on Bathroom Geyser')
                        playsound("sounds/turning_on_the_geyser.mp3")
                        time.sleep(1)
                        playsound("sounds/device_up.mp3")
                        command_result = ""

                elif command_result == 7:

                    u = 'u9'
                    d = 'd9'

                    if ai.state[9] == 1:
                        ai.command(d)
                        print('Turning off Water Pump')
                        playsound("sounds/turning_off_water_pump.mp3")
                        time.sleep(1)
                        playsound("sounds/device_down.mp3")
                        command_result = ""

                    elif ai.state[9] == 0:
                        ai.command(u)
                        print('Turning on Water Pump')
                        playsound("sounds/turning_on_water_pump.mp3")
                        time.sleep(1)
                        playsound("sounds/device_up.mp3")
                        command_result = ""

                elif command_result == 8:

                    u = 'uA'
                    d = 'dA'

                    if ai.state[10] == 1:
                        ai.command(d)
                        print('Turning off Socket One')
                        playsound("sounds/turning_off_socket_one.mp3")
                        time.sleep(1)
                        playsound("sounds/device_down.mp3")
                        command_result = ""

                    elif ai.state[10] == 0:
                        ai.command(u)
                        print('Turning on Socket One')
                        playsound("sounds/turning_on_socket_one.mp3")
                        time.sleep(1)
                        playsound("sounds/device_up.mp3")
                        command_result = ""

                elif command_result == 9:

                    u = 'uB'
                    d = 'dB'

                    if ai.state[11] == 1:
                        ai.command(d)
                        print('Turning off Socket Two')
                        playsound("sounds/turning_off_socket_two.mp3")
                        time.sleep(1)
                        playsound("sounds/device_down.mp3")
                        command_result = ""

                    elif ai.state[11] == 0:
                        ai.command(u)
                        print('Turning on Socket Two')
                        playsound("sounds/turning_on_socket_two.mp3")
                        time.sleep(1)
                        playsound("sounds/device_up.mp3")
                        command_result = ""

                elif command_result == 10:

                    u = 'uC'

                    ai.command(u)
                    print('Opeaning the door')
                    playsound("sounds/unlocking_the_door.mp3")
                    time.sleep(1)
                    playsound("sounds/device_down.mp3")
                    command_result = ""

                elif command_result == 11:

                    d = 'dC'
                    playsound("sounds/locking_the_door.mp3")
                    time.sleep(1)
                    playsound("sounds/device_down.mp3")
                    ai.command(d)
                    print('Closing the door')
                    command_result = None

                elif command_result == 12:

                    u = 'uD'
                    playsound("sounds/supplying_the_main_power.mp3")
                    time.sleep(1)
                    playsound("sounds/device_down.mp3")
                    ai.command(u)
                    print('Main power is now ON')
                    command_result = None

                elif command_result == 13:

                    d = 'dD'
                    playsound("sounds/cutting_the_main_power.mp3")
                    time.sleep(1)
                    playsound("sounds/device_down.mp3")
                    ai.command(d)
                    print('Main power is now SHUT')
                    command_result = None

                awake = False

except KeyboardInterrupt:
    print('stopping ...')
finally:
    if porcupine_wakeword is not None:
        porcupine_wakeword.delete()

    if audio_stream is not None:
        audio_stream.close()

    if pa is not None:
        pa.terminate()
