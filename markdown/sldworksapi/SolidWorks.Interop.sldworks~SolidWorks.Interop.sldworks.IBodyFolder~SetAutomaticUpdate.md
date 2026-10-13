---
title: "SetAutomaticUpdate Method (IBodyFolder)"
project: "SOLIDWORKS API Help"
interface: "IBodyFolder"
member: "SetAutomaticUpdate"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~SetAutomaticUpdate.html"
---

# SetAutomaticUpdate Method (IBodyFolder)

Sets whether to automatically update cut lists.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetAutomaticUpdate( _
   ByVal Update As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBodyFolder
Dim Update As System.Boolean
Dim value As System.Boolean

value = instance.SetAutomaticUpdate(Update)
```

### C#

```csharp
System.bool SetAutomaticUpdate(
   System.bool Update
)
```

### C++/CLI

```cpp
System.bool SetAutomaticUpdate(
   System.bool Update
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Update`: True to automatically update cut lists, false to update them manually

### Return Value

True if successful, false if not

## VBA Syntax

See [BodyFolder::SetAutomaticUpdate](ms-its:sldworksapivb6.chm::/sldworks~BodyFolder~SetAutomaticUpdate.html).

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
[IBodyFolder::GetAutomaticUpdate Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~GetAutomaticUpdate.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
