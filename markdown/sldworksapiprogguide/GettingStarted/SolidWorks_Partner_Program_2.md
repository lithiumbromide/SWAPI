---
title: "SOLIDWORKS Partner Program"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/GettingStarted/SolidWorks_Partner_Program_2.htm"
---

# SOLIDWORKS Partner Program

```vb
 As of SOLIDWORKS 2021, SOLIDWORKS Partners must register their products with the SOLIDWORKS Partner Program. The SOLIDWORKS Partner Program team, in turn, provides license keys and a sample add-in that registered SOLIDWORKS Partners can modify to create their add-ins. The sample add-in:
```

- ```vb
  Implements both  ISwAddin and ISwPEManager.
  ```
- ```vb
  Employs an  ISwPEClassFactory callback object that allows the add-in to transfer a license key to SOLIDWORKS for entitlement verification and receive back an  ISwPEToken object.
  ```

```vb
 License keys provide better quality and security and may be extended in the future to afford SOLIDWORKS Partners special entitlements.
 SOLIDWORKS Partners can obtain more information from the SOLIDWORKS Partner Team by emailing SOLIDWORKS.PartnerProgram@3ds.com.
 During the load of the partner's add-in, SOLIDWORKS Desktop or SOLIDWORKS Connected uses the partner's license key to verify entitlement and determine how to display the partner's add-in in the Tools > Add-Ins dialog:
      Partner Gold Add-ins
      Partner Solution Add-ins
      Other Add-ins - Unregistered add-ins
```

##### For SOLIDWORKS Desktop...

SOLIDWORKS lists the registered partner add-in under**Partner Gold Add-ins**or**Partner Solution Add-ins**according to its verified entitlement. If the
entitlement type in the license key does not match the current registry value,
SOLIDWORKS still lists the add-in according tothe entitlement in the license key. The registry is updated with the
entitlement in the license key. To see the add-in listed under its proper entitlement, re-open Tools > Add-Ins .

- or -

SOLIDWORKS lists the add-in under**Other Add-ins**because:

- The add-in does not send a license key back to
  SOLIDWORKS at load time.
- The add-in does not implement ISwPEManager.
- Thelicense key passed its expiration date.
- ```vb
  One or more license key  tokens do not match corresponding values in the registry (add-in GUID, add-in name, or SOLIDWORKS version).
  ```

##### For SOLIDWORKS Connected...

SOLIDWORKS lists the partner add-in under**Partner Gold
Add-ins**or**Partner Solution Add-ins**according to its verified entitlement.
If the entitlement type in the license key does not match the current registry
value, SOLIDWORKS still lists the add-in according tothe entitlement in the license key. The registry is updated with the
entitlement in the license key. To see the add-in listed under its proper
entitlement, re-open Tools > Add-ins .

- or -

SOLIDWORKS lists the add-in under**Other Addin-ins**if the add-in does not implement ISwPEManager or the add-in does not send a
license key to SOLIDWORKS. In either case, the SOLIDWORKS Partner may be in
violation of its partner agreement with SOLIDWORKS.

- or -

SOLIDWORKS lists the add-in under**Other Add-ins**but does not load it (unchecked) because:

- ```vb
  The license key passed its expiration date, or the license key is not valid for the current release of SOLIDWORKS Connected.
  ```
- ```vb
  One or more license key  tokens do not match corresponding values in the registry (add-in GUID, add-in name, or SOLIDWORKS version).
  ```
