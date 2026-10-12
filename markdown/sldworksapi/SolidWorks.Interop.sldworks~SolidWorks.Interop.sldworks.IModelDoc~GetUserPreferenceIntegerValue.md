---
title: "GetUserPreferenceIntegerValue Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "GetUserPreferenceIntegerValue"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~GetUserPreferenceIntegerValue.html"
---

# GetUserPreferenceIntegerValue Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::GetUserPreferenceIntegerValue](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetUserPreferenceIntegerValue.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetUserPreferenceIntegerValue( _
   ByVal UserPreferenceValue As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim UserPreferenceValue As System.Integer
Dim value As System.Integer

value = instance.GetUserPreferenceIntegerValue(UserPreferenceValue)
```

### C#

```csharp
System.int GetUserPreferenceIntegerValue(
   System.int UserPreferenceValue
)
```

### C++/CLI

```cpp
System.int GetUserPreferenceIntegerValue(
   System.int UserPreferenceValue
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UserPreferenceValue`:

## VBA Syntax

See [ModelDoc::GetUserPreferenceIntegerValue](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~GetUserPreferenceIntegerValue.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
