---
title: "PathName Property (IExternalReference)"
project: ""
interface: "IExternalReference"
member: "PathName"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IExternalReference~PathName.html"
---

# PathName Property (IExternalReference)

Gets or sets the path of the external reference.

## Syntax

### Visual Basic

```vb
Property PathName As System.String
```

### C#

```csharp
System.string PathName {get; set;}
```

### JScript

```
function get,set PathName : System.String
```

### Managed Extensions for C++

```
__property System.string* get_PathName();
__property void set_PathName(
   System.string* value
);
```

### C++/CLI

```cpp
property System.String^ PathName {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Path of the external reference

## Examples

This code snippet shows how to get the external references and their names and paths.

##### COM native C++

_variant_t pVariantArray = dsDoc->GetExternalReferences();
if( V_VT( &pVariantArray ) != VT_EMPTY )
{
IExternalReferencePtr *ExtRef = NULL;
int countOfExtRef = 0;
[TypeConverter::convertVariantArrayToPtrArray](GettingStarted-draftsightapi.html#convertVariantArrayToPtrArray)<IExternalReferencePtr, IExternalReference>( pVariantArray, ExtRef, countOfExtRef );

bstr_t xRefPath = ExtRef[i]->GetPathName();
}
delete[] ExtRef;

## See Also

[IExternalReference Interface](Interop.dsAutomation~Interop.dsAutomation.IExternalReference.html)
[IExternalReference Members](Interop.dsAutomation~Interop.dsAutomation.IExternalReference_members.html)
[IExternalReference::Name Property](Interop.dsAutomation~Interop.dsAutomation.IExternalReference~Name.html)

## Availability

DraftSight V1R1
