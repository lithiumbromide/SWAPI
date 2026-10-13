---
title: "Command Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "Command"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~Command.html"
---

# Command Method (ISldWorks)

Opens the specified dialog or file.

## Syntax

### Visual Basic (Declaration)

```vb
Function Command( _
   ByVal Command As System.Integer, _
   ByVal Args As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim Command As System.Integer
Dim Args As System.Object
Dim value As System.Object

value = instance.Command(Command, Args)
```

### C#

```csharp
System.object Command(
   System.int Command,
   System.object Args
)
```

### C++/CLI

```cpp
System.Object^ Command(
   System.int Command,
   System.Object^ Args
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Command`: Command as defined by [swCommand_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCommand_e.html)
- `Args`: See Remarks

## VBA Syntax

See [SldWorks::Command](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~Command.html).

## Remarks

| If command specified is... | Then pass... |
| --- | --- |
| swOpenHTMLHelp | Path and filename for the compiled HTML file (has .chm filename extension) |
| swFileOpen swFileNew swOpenRecentFile | Empty VARIANT; for example: VARIANT args; V_VT(&args) = VT_EMPTY; // Call Command API and open the File, Open dialog swApp->Command(0, args, &retval); |

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
