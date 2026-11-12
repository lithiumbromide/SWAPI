---
title: "GetUserPreferenceStringValue Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "GetUserPreferenceStringValue"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~GetUserPreferenceStringValue.html"
---

# GetUserPreferenceStringValue Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::GetUserPreferenceStringValue](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetUserPreferenceStringValue.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetUserPreferenceStringValue( _
   ByVal UserPreference As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim UserPreference As System.Integer
Dim value As System.String

value = instance.GetUserPreferenceStringValue(UserPreference)
```

### C#

```csharp
System.string GetUserPreferenceStringValue(
   System.int UserPreference
)
```

### C++/CLI

```cpp
System.String^ GetUserPreferenceStringValue(
   System.int UserPreference
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UserPreference`:

## VBA Syntax

See [ModelDoc::GetUserPreferenceStringValue](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~GetUserPreferenceStringValue.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
