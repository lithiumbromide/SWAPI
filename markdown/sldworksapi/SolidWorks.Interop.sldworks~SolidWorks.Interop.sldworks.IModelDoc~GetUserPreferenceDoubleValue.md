---
title: "GetUserPreferenceDoubleValue Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "GetUserPreferenceDoubleValue"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~GetUserPreferenceDoubleValue.html"
---

# GetUserPreferenceDoubleValue Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::GetUserPreferenceDoubleValue](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetUserPreferenceDoubleValue.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetUserPreferenceDoubleValue( _
   ByVal UserPreferenceValue As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim UserPreferenceValue As System.Integer
Dim value As System.Double

value = instance.GetUserPreferenceDoubleValue(UserPreferenceValue)
```

### C#

```csharp
System.double GetUserPreferenceDoubleValue(
   System.int UserPreferenceValue
)
```

### C++/CLI

```cpp
System.double GetUserPreferenceDoubleValue(
   System.int UserPreferenceValue
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UserPreferenceValue`:

## VBA Syntax

See [ModelDoc::GetUserPreferenceDoubleValue](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~GetUserPreferenceDoubleValue.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
