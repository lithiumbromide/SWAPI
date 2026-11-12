using System;
using System.Diagnostics;
using System.Drawing;
using System.Drawing.Imaging;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.InteropServices;
using Microsoft.Win32;
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using SolidWorks.Interop.swpublished;
[assembly: ComVisible(false)]
namespace SolidWorksAddin
{
    [ComVisible(true)]
    [Guid("00000000-0000-0000-0000-000000000000")]
    public class SwAddin : ISwAddin
    {
        private const string Title = "SolidWorksAddin";
        private const string Description = "SolidWorksAddin";
        private const int MainGroupId = 1;
        private const int RunCommandId = 1;
        private static readonly int[] CommandIds = { RunCommandId };
        private static readonly int[] IconSizes = { 20, 32, 40, 64, 96, 128 };
        private static readonly Guid ControlPlaceholder = new Guid("00000000-0000-0000-0000-000000000001");
        private ISldWorks swApp;
        private ICommandManager commandManager;
        private int cookie;
        private ITaskpaneView taskPaneView;
        private TaskPaneControl taskPaneControl;
        [ComRegisterFunction]
        public static void RegisterFunction(Type t)
        {
            if (t.GUID == Guid.Empty || typeof(TaskPaneControl).GUID == ControlPlaceholder)
            {
                throw new InvalidOperationException("Replace the placeholder GUIDs of SwAddin and TaskPaneControl with new GUIDs before registering.");
            }
            using (RegistryKey key = Registry.LocalMachine.CreateSubKey(AddinKey(t)))
            {
                key.SetValue(null, 0);
                key.SetValue("Description", Description);
                key.SetValue("Title", Title);
            }
            using (RegistryKey key = Registry.CurrentUser.CreateSubKey(StartupKey(t)))
            {
                key.SetValue(null, 1, RegistryValueKind.DWord);
            }
        }
        [ComUnregisterFunction]
        public static void UnregisterFunction(Type t)
        {
            Registry.LocalMachine.DeleteSubKeyTree(AddinKey(t), false);
            Registry.CurrentUser.DeleteSubKeyTree(StartupKey(t), false);
        }
        private static string AddinKey(Type t) => @"SOFTWARE\SolidWorks\Addins\{" + t.GUID.ToString() + "}";
        private static string StartupKey(Type t) => @"Software\SolidWorks\AddInsStartup\{" + t.GUID.ToString() + "}";
        public bool ConnectToSW(object ThisSW, int Cookie)
        {
            swApp = (ISldWorks)ThisSW;
            cookie = Cookie;
            swApp.SetAddinCallbackInfo2(0, this, cookie);
            commandManager = swApp.GetCommandManager(cookie);
            AddCommands();
            AddTaskPane();
            return true;
        }
        public bool DisconnectFromSW()
        {
            RemoveTaskPane();
            commandManager.RemoveCommandGroup2(MainGroupId, true);
            Marshal.ReleaseComObject(commandManager);
            commandManager = null;
            Marshal.ReleaseComObject(swApp);
            swApp = null;
            GC.Collect();
            GC.WaitForPendingFinalizers();
            GC.Collect();
            GC.WaitForPendingFinalizers();
            return true;
        }
        private void AddCommands()
        {
            object registryIds;
            bool ignorePrevious = false;
            if (commandManager.GetGroupDataFromRegistry(MainGroupId, out registryIds))
            {
                int[] storedIds = registryIds as int[];
                ignorePrevious = storedIds == null || !storedIds.OrderBy(id => id).SequenceEqual(CommandIds.OrderBy(id => id));
            }
            int errors = 0;
            ICommandGroup group = commandManager.CreateCommandGroup2(MainGroupId, Title, Description, Description, -1, ignorePrevious, ref errors);
            if (group == null)
            {
                Debug.WriteLine(Title + ": CreateCommandGroup2 failed with " + (swCreateCommandGroupErrors)errors);
                return;
            }
            group.AddCommandItem2("Run", -1, "Run " + Title, "Run", -1, nameof(OnRun), nameof(OnRunEnable), RunCommandId, (int)swCommandItemType_e.swMenuItem);
            group.HasMenu = true;
            group.HasToolbar = false;
            group.Activate();
        }
        private void AddTaskPane()
        {
            taskPaneView = swApp.CreateTaskpaneView3(TaskPaneIcons(), Title);
            if (taskPaneView == null)
            {
                Debug.WriteLine(Title + ": CreateTaskpaneView3 returned null");
                return;
            }
            taskPaneControl = taskPaneView.AddControl(TaskPaneControl.ControlProgId, "") as TaskPaneControl;
            if (taskPaneControl == null)
            {
                Debug.WriteLine(Title + ": AddControl failed; register the assembly with RegAsm /codebase");
                return;
            }
            taskPaneControl.RunClicked += OnTaskPaneRun;
        }
        private static string[] TaskPaneIcons()
        {
            string folder = Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location);
            string[] shipped = IconSizes.Select(size => Path.Combine(folder, "TaskPane_" + size + ".png")).ToArray();
            if (shipped.All(File.Exists))
            {
                return shipped;
            }
            string generated = Path.Combine(Path.GetTempPath(), Title);
            Directory.CreateDirectory(generated);
            return IconSizes.Select(size => GenerateIcon(generated, size)).ToArray();
        }
        private static string GenerateIcon(string folder, int size)
        {
            string path = Path.Combine(folder, "TaskPane_" + size + ".png");
            using (Bitmap bitmap = new Bitmap(size, size))
            using (Graphics graphics = Graphics.FromImage(bitmap))
            {
                graphics.Clear(Color.FromArgb(192, 192, 192));
                graphics.FillRectangle(Brushes.SteelBlue, size / 5, size / 5, size * 3 / 5, size * 3 / 5);
                bitmap.Save(path, ImageFormat.Png);
            }
            return path;
        }
        private void RemoveTaskPane()
        {
            if (taskPaneControl != null)
            {
                taskPaneControl.RunClicked -= OnTaskPaneRun;
                taskPaneControl = null;
            }
            if (taskPaneView != null)
            {
                taskPaneView.DeleteView();
                Marshal.ReleaseComObject(taskPaneView);
                taskPaneView = null;
            }
        }
        public void OnRun()
        {
            Execute(string.Empty);
        }
        public int OnRunEnable()
        {
            return swApp.ActiveDoc == null ? 0 : 1;
        }
        private void OnTaskPaneRun(object sender, EventArgs e)
        {
            Execute(taskPaneControl.InputText);
        }
        private void Execute(string input)
        {
            IModelDoc2 model = swApp.ActiveDoc as IModelDoc2;
            if (model == null)
            {
                Notify("Open a document first.", swMessageBoxIcon_e.swMbWarning);
                return;
            }
            Notify(model.GetTitle() + " " + input, swMessageBoxIcon_e.swMbInformation);
        }
        private void Notify(string message, swMessageBoxIcon_e icon)
        {
            swApp.SendMsgToUser2(message, (int)icon, (int)swMessageBoxBtn_e.swMbOk);
        }
    }
}
