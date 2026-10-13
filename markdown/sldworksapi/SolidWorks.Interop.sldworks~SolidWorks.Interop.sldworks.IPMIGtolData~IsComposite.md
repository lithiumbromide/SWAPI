---
title: "IsComposite Method (IPMIGtolData)"
project: "SOLIDWORKS API Help"
interface: "IPMIGtolData"
member: "IsComposite"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolData~IsComposite.html"
---

# IsComposite Method (IPMIGtolData)

Gets whether this PMI Gtol combines the symbols of two frames.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsComposite() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIGtolData
Dim value As System.Boolean

value = instance.IsComposite()
```

### C#

```csharp
System.bool IsComposite()
```

### C++/CLI

```cpp
System.bool IsComposite();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if a composite frame, false if not

## VBA Syntax

See [PMIGtolData::IsComposite](ms-its:sldworksapivb6.chm::/sldworks~PMIGtolData~IsComposite.html).

## Examples

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html) example.

## See Also

[IPMIGtolData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolData.html)
[IPMIGtolData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
