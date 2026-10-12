---
title: "IsCommandEnabled Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "IsCommandEnabled"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IsCommandEnabled.html"
---

# IsCommandEnabled Method (ISldWorks)

Gets whether the specified command is enabled.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsCommandEnabled( _
   ByVal CommandID As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim CommandID As System.Integer
Dim value As System.Boolean

value = instance.IsCommandEnabled(CommandID)
```

### C#

```csharp
System.bool IsCommandEnabled(
   System.int CommandID
)
```

### C++/CLI

```cpp
System.bool IsCommandEnabled(
   System.int CommandID
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CommandID`: Command ID as defined [swCommands_e](ms-its:swcommands.chm::/SOLIDWORKS.Interop.swcommands.html) (see Remarks)

### Return Value

True if the command is enabled, false if not

## VBA Syntax

See [SldWorks::IsCommandEnabled](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~IsCommandEnabled.html).

## Remarks

Before using this method, you must add a reference to the version-specific SOLIDWORKS Commands type library to access the SOLIDWORKS commands.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::RunCommand Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RunCommand.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
