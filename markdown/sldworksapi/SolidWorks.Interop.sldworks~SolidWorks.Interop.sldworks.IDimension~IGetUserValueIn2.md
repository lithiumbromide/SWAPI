---
title: "IGetUserValueIn2 Method (IDimension)"
project: "SOLIDWORKS API Help"
interface: "IDimension"
member: "IGetUserValueIn2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IGetUserValueIn2.html"
---

# IGetUserValueIn2 Method (IDimension)

Gets the value of this dimension in the units of the specified document.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetUserValueIn2( _
   ByVal Doc As ModelDoc2 _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDimension
Dim Doc As ModelDoc2
Dim value As System.Double

value = instance.IGetUserValueIn2(Doc)
```

### C#

```csharp
System.double IGetUserValueIn2(
   ModelDoc2 Doc
)
```

### C++/CLI

```cpp
System.double IGetUserValueIn2(
   ModelDoc2^ Doc
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Doc`: [Document](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) whose units you want to use

### Return Value

Value of this dimension in the units of the document specified by Doc

## VBA Syntax

See [Dimension::IGetUserValueIn2](ms-its:sldworksapivb6.chm::/sldworks~Dimension~IGetUserValueIn2.html).

## See Also

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.html)
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.html)
[IDimension::GetUserValueIn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetUserValueIn.html)
[IDimension::GetSystemValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetSystemValue3.html)
[IDimension::IGetSystemValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IGetSystemValue3.html)
[IDimension::ISetSystemValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ISetSystemValue3.html)
[IDimension::ISetUserValueIn3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ISetUserValueIn3.html)
[IDimension::SetSystemValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetSystemValue3.html)
[IDimension::SetUserValueIn2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetUserValueIn2.html)
[IDimension::GetValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetValue3.html)
[IDimension::IGetValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IGetValue3.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
