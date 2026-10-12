---
title: "Monitor Loading of .NET Interop Assemblies"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/Monitor_Loading_of_.NET_Interop_Assemblies.htm"
---

# Monitor Loading of .NET Interop Assemblies

You can monitor which .NET interop assemblies are loaded by the .NET runtime.

The subsystem of the .NET runtime that handles resolving, loading, and binding to assemblies is called Fusion and includes a log viewer. Invoke the log viewer in your version of Microsoft .NET framework as follows:

| If you have Microsoft .NET Framework Version... | Run... |
| --- | --- |
| 2.0 or 3.5 | Fuslogvw.exe in Start Menu > All Programs > Microsoft .NET Framework SDK v2.0 > SDK Command Prompt |
| 4.0 | Fuslogvw.exe in Start Menu > All Programs > Microsoft Visual Studio 2010 > Visual Studio Tools > Visual Studio Command Prompt |

The log viewer allows you to monitor which interop assemblies .NET is looking for and which ones it actually finds and loads. This includes the .NET primary interop assemblies needed by a SOLIDWORKS, SOLIDWORKS PDM Professional, etc.

This tool is helpful in determining why .NET did not find a particular assembly or found the wrong one.
