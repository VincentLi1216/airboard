import unittest
from unittest import mock
import numpy as np

from utils import capture_frame
from utils import color_map
from utils import find_files_in_dir

class TestCaptureFrames(unittest.TestCase):
    @mock.patch('os.path.exists')
    @mock.patch('utils.capture_frame.VideoFileClip')
    @mock.patch('utils.capture_frame.Image')
    @mock.patch('os.path.join')
    def test_capture_frames(self, mock_join, mock_image, mock_clip, mock_exists):
        # Mocking the os.path.exists to always return True
        mock_exists.return_value = True

        # Mocking the VideoFileClip object
        mock_clip_instance = mock.MagicMock()
        mock_clip_instance.duration = 20
        mock_clip.return_value = mock_clip_instance

        # Mocking the Image object
        mock_image_instance = mock.MagicMock()
        mock_image.fromarray.return_value = mock_image_instance

        # Mocking the os.path.join function
        mock_join.return_value = "/fake/path"

        # Call the function with the mock objects
        capture_frame.capture_frames(
            "/fake/video/path", "/fake/output/folder", 5)

        # Assert that the VideoFileClip was called with the correct video path
        mock_clip.assert_called_once_with("/fake/video/path")

        # Assert that the Image.fromarray was called (20/5) + 1 times
        self.assertEqual(mock_image.fromarray.call_count, int(mock_clip_instance.duration // 5) + 1)

        # Assert that the image save method was called (20/5) + 1 times
        self.assertEqual(mock_image_instance.save.call_count, int(mock_clip_instance.duration // 5) + 1)

    @mock.patch('os.path.exists')
    def test_capture_frames_video_not_exists(self, mock_exists):
        # Mocking the os.path.exists to return False
        mock_exists.return_value = False

        # Call the function with the mock objects
        capture_frame.capture_frames(
            "/fake/video/path", "/fake/output/folder", 5)

        # Assert that the function returned early
        mock_exists.assert_called_once_with("/fake/video/path")

class TestColorMap(unittest.TestCase):
    @mock.patch('cv2.cvtColor')
    @mock.patch('cv2.applyColorMap')
    @mock.patch('cv2.addWeighted')
    def test_color_map(self, mock_addWeighted, mock_applyColorMap, mock_cvtColor):
        # Mocking the cv2.cvtColor function
        mock_cvtColor.return_value = np.array([[0, 0, 0]])

        # Mocking the cv2.applyColorMap function
        mock_applyColorMap.return_value = np.array([[0, 0, 0]])

        # Mocking the cv2.addWeighted function
        mock_addWeighted.return_value = np.array([[0, 0, 0]])

        # Call the function with a 3D array
        img = np.array([[[0, 0, 0]]])
        result = color_map.color_map(img)

        # Assert that the cv2.cvtColor was called once
        mock_cvtColor.assert_called_once()

        # Assert that the cv2.applyColorMap was called once
        mock_applyColorMap.assert_called_once()

        # Assert that the cv2.addWeighted was called once
        mock_addWeighted.assert_called_once()

    @mock.patch('cv2.cvtColor')
    @mock.patch('cv2.applyColorMap')
    @mock.patch('cv2.addWeighted')
    def test_apply_colored_mask_on_image(self, mock_addWeighted, mock_applyColorMap, mock_cvtColor):
        # Mocking the cv2.cvtColor function
        mock_cvtColor.return_value = np.array([[0, 0, 0]])

        # Mocking the cv2.applyColorMap function
        mock_applyColorMap.return_value = np.array([[0, 0, 0]])

        # Mocking the cv2.addWeighted function
        mock_addWeighted.return_value = np.array([[0, 0, 0]])

        # Call the function with a 3D array
        img = np.array([[[0, 0, 0]]])
        mask = np.array([[0]])
        result = color_map.apply_colored_mask_on_image(img, mask)

        # Assert that the cv2.applyColorMap was called once
        mock_applyColorMap.assert_called_once()

        # Assert that the cv2.addWeighted was called once
        mock_addWeighted.assert_called_once()

class TestFindFilesInDir(unittest.TestCase):
    @mock.patch('os.listdir')
    @mock.patch('os.path.join')
    @mock.patch('os.path.isfile')
    def test_find_files_in_dir(self, mock_isfile, mock_join, mock_listdir):
        # Mocking the os.listdir function
        mock_listdir.return_value = ['file1.txt', 'file2.jpg', 'file3.txt']

        # Mocking the os.path.join function
        mock_join.side_effect = lambda a, b: a + '/' + b

        # Mocking the os.path.isfile function
        mock_isfile.return_value = True

        # Call the function with the mock objects
        result = find_files_in_dir.find_files_in_dir('/fake/path', ['.txt'])

        # Assert that the result is as expected
        self.assertEqual(result, ['/fake/path/file1.txt', '/fake/path/file3.txt'])

    @mock.patch('os.listdir')
    @mock.patch('os.path.join')
    @mock.patch('os.path.isfile')
    def test_find_files_in_dir_no_files(self, mock_isfile, mock_join, mock_listdir):
        # Mocking the os.listdir function
        mock_listdir.return_value = []

        # Call the function with the mock objects
        result = find_files_in_dir.find_files_in_dir('/fake/path', ['.txt'])

        # Assert that the result is an empty list
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
