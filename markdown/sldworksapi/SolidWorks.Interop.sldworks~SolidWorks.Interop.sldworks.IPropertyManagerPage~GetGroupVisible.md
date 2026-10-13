---
title: "GetGroupVisible Method (IPropertyManagerPage)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPage"
member: "GetGroupVisible"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage~GetGroupVisible.html"
---

# GetGroupVisible Method (IPropertyManagerPage)

Obsolete. Not superseded.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetGroupVisible( _
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

value = instance.GetGroupVisible(GroupID, Status)
```

### C#

```csharp
System.bool GetGroupVisible(
   System.int GroupID,
   out System.int Status
)
```

### C++/CLI

```cpp
System.bool GetGroupVisible(
   System.int GroupID,
   [Out] System.int Status
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `GroupID`:
- `Status`:

## VBA Syntax

See [PropertyManagerPage::GetGroupVisible](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPage~GetGroupVisible.html).

## See Also

[IPropertyManagerPage Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage.html)
[IPropertyManagerPage Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage_members.html)
