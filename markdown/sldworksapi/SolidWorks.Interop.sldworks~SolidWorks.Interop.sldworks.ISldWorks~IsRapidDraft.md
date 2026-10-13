---
title: "IsRapidDraft Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "IsRapidDraft"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IsRapidDraft.html"
---

# IsRapidDraft Method (ISldWorks)

Gets whether the specified drawing file is in SOLIDWORKS Detached format.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsRapidDraft( _
   ByVal FileName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim FileName As System.String
Dim value As System.Boolean

value = instance.IsRapidDraft(FileName)
```

### C#

```csharp
System.bool IsRapidDraft(
   System.string FileName
)
```

### C++/CLI

```cpp
System.bool IsRapidDraft(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Name of the drawing file

### Return Value

True if the file is in RapidDraft format, false if not

## VBA Syntax

See [SldWorks::IsRapidDraft](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~IsRapidDraft.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
