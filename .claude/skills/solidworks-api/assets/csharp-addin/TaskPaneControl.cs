using System;
using System.Runtime.InteropServices;
using System.Windows.Forms;
namespace SolidWorksAddin
{
    [ComVisible(true)]
    [Guid("00000000-0000-0000-0000-000000000001")]
    [ProgId(ControlProgId)]
    public class TaskPaneControl : UserControl
    {
        public const string ControlProgId = "SolidWorksAddin.TaskPaneControl";
        private readonly TextBox input = new TextBox();
        private readonly Button runButton = new Button();
        public event EventHandler RunClicked;
        public TaskPaneControl()
        {
            input.Dock = DockStyle.Top;
            runButton.Dock = DockStyle.Top;
            runButton.Text = "Run";
            runButton.Click += (sender, e) => RunClicked?.Invoke(this, EventArgs.Empty);
            Controls.Add(runButton);
            Controls.Add(input);
        }
        public string InputText => input.Text;
    }
}
