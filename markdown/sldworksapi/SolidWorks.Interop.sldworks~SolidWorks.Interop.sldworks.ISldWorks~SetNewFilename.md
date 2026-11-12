---
title: "SetNewFilename Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "SetNewFilename"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetNewFilename.html"
---

# SetNewFilename Method (ISldWorks)

Sets the name of the new SOLIDWORKS file.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetNewFilename( _
   ByVal FileName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim FileName As System.String
Dim value As System.Boolean

value = instance.SetNewFilename(FileName)
```

### C#

```csharp
System.bool SetNewFilename(
   System.string FileName
)
```

### C++/CLI

```cpp
System.bool SetNewFilename(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Path and file name for new SOLIDWORKS file

### Return Value

True if the name of the new SOLIDWORKS file is set, false if not

## VBA Syntax

See [SldWorks::SetNewFilename](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~SetNewFilename.html).

## Remarks

Use with SldWorks [FileNewPreNotifyEventHandler](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldWorksEvents_FileNewPreNotifyEventHandler.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
