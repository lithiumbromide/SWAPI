using System;
using System.Runtime.InteropServices;
using EPDM.Interop.epdm;
using EPDM.Interop.EPDMResultCode;
namespace PdmTool
{
    internal static class Program
    {
        [STAThread]
        private static int Main(string[] args)
        {
            if (args.Length < 3)
            {
                Console.Error.WriteLine("usage: PdmTool <vault view name> <variable> <file path>...");
                return 2;
            }
            IEdmVault5 vault = new EdmVault5();
            try
            {
                vault.LoginAuto(args[0], 0);
                var exitCode = 0;
                Console.WriteLine(string.Join("\t", "Path", "Revision", "State", args[1]));
                for (var i = 2; i < args.Length; i++)
                {
                    try
                    {
                        IEdmFolder5 folder;
                        var file = vault.GetFileFromPath(args[i], out folder);
                        if (file == null)
                        {
                            Console.Error.WriteLine("not a vault file: " + args[i]);
                            exitCode = 1;
                            continue;
                        }
                        Console.WriteLine(string.Join("\t", args[i], file.CurrentRevision, file.CurrentState.Name, ReadVariable(file, args[1])));
                    }
                    catch (COMException ex)
                    {
                        Console.Error.WriteLine(args[i] + ": " + Describe(vault, ex));
                        exitCode = 1;
                    }
                }
                return exitCode;
            }
            catch (COMException ex)
            {
                Console.Error.WriteLine(Describe(vault, ex));
                return 1;
            }
        }
        private static string ReadVariable(IEdmFile5 file, string name)
        {
            var variables = (IEdmEnumeratorVariable8)file.GetEnumeratorVariable();
            try
            {
                object value;
                if (!variables.GetVar(name, "@", out value))
                {
                    variables.GetVar(name, "", out value);
                }
                return Convert.ToString(value);
            }
            finally
            {
                variables.CloseFile(false);
            }
        }
        private static string Describe(IEdmVault5 vault, COMException ex)
        {
            if (ex.ErrorCode == (int)EdmResultErrorCodes_e.E_EDM_CANT_OPEN_DATABASE)
            {
                return "cannot open the vault database; check the vault view name";
            }
            string name;
            string description;
            vault.GetErrorString(ex.ErrorCode, out name, out description);
            return string.Format("0x{0:X8} {1}: {2}", ex.ErrorCode, name, description);
        }
    }
}
