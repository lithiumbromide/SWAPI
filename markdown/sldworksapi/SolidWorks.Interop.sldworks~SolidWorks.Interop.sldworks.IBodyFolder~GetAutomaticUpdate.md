---
title: "GetAutomaticUpdate Method (IBodyFolder)"
project: "SOLIDWORKS API Help"
interface: "IBodyFolder"
member: "GetAutomaticUpdate"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~GetAutomaticUpdate.html"
---

# GetAutomaticUpdate Method (IBodyFolder)

Gets whether to automatically update cut lists.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAutomaticUpdate() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBodyFolder
Dim value As System.Boolean

value = instance.GetAutomaticUpdate()
```

### C#

```csharp
System.bool GetAutomaticUpdate()
```

### C++/CLI

```cpp
System.bool GetAutomaticUpdate();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True to automatically update cut lists, false to update them manually

## VBA Syntax

See [BodyFolder::GetAutomaticUpdate](ms-its:sldworksapivb6.chm::/sldworks~BodyFolder~GetAutomaticUpdate.html).

## Examples

See the [IBodyFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder.html) examples.

## Remarks

| To update cut lists... | Call... |
| --- | --- |
| Manually | IBodyFolder::UpdateCutList |
| Automatically | IBodyFolder::SetAutomaticUpdate |

## See Also

[IBodyFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder.html)
[IBodyFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
