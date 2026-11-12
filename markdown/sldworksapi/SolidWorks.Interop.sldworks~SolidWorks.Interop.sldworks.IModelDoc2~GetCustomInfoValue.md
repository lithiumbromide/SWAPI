---
title: "GetCustomInfoValue Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "GetCustomInfoValue"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetCustomInfoValue.html"
---

# GetCustomInfoValue Method (IModelDoc2)

Obsolete. Superseded by [IModelDocExtension::CustomPropertyManager](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~CustomPropertyManager.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCustomInfoValue( _
   ByVal Configuration As System.String, _
   ByVal FieldName As System.String _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Configuration As System.String
Dim FieldName As System.String
Dim value As System.String

value = instance.GetCustomInfoValue(Configuration, FieldName)
```

### C#

```csharp
System.string GetCustomInfoValue(
   System.string Configuration,
   System.string FieldName
)
```

### C++/CLI

```cpp
System.String^ GetCustomInfoValue(
   System.String^ Configuration,
   System.String^ FieldName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Configuration`:
- `FieldName`:

## VBA Syntax

See [ModelDoc2::GetCustomInfoValue](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~GetCustomInfoValue.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
