---
title: "GetGroupExpanded Method (IPropertyManagerPage)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPage"
member: "GetGroupExpanded"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage~GetGroupExpanded.html"
---

# GetGroupExpanded Method (IPropertyManagerPage)

Obsolete. Not superseded.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetGroupExpanded( _
   ByVal GroupID As System.Integer, _
   ByRef Status As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage
Dim GroupID As System.Integer
Dim Status As System.Integer
Dim value As System.Boolean

value = instance.GetGroupExpanded(GroupID, Status)
```

### C#

```csharp
System.bool GetGroupExpanded(
   System.int GroupID,
   out System.int Status
)
```

### C++/CLI

```cpp
System.bool GetGroupExpanded(
   System.int GroupID,
   [Out] System.int Status
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `GroupID`:
- `Status`:

## VBA Syntax

See [PropertyManagerPage::GetGroupExpanded](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPage~GetGroupExpanded.html).

## See Also

[IPropertyManagerPage Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage.html)
[IPropertyManagerPage Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage_members.html)
